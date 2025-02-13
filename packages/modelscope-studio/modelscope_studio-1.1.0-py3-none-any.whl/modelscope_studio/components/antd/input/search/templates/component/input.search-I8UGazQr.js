import { i as ue, a as M, r as de, b as fe, g as me, w as P, c as _e } from "./Index-BD2Gw4Ky.js";
const v = window.ms_globals.React, ce = window.ms_globals.React.forwardRef, N = window.ms_globals.React.useRef, te = window.ms_globals.React.useState, W = window.ms_globals.React.useEffect, ne = window.ms_globals.React.useMemo, B = window.ms_globals.ReactDOM.createPortal, pe = window.ms_globals.internalContext.useContextPropsContext, q = window.ms_globals.internalContext.ContextPropsProvider, he = window.ms_globals.antd.Input;
var ge = /\s/;
function we(e) {
  for (var t = e.length; t-- && ge.test(e.charAt(t)); )
    ;
  return t;
}
var xe = /^\s+/;
function be(e) {
  return e && e.slice(0, we(e) + 1).replace(xe, "");
}
var z = NaN, ye = /^[-+]0x[0-9a-f]+$/i, Ee = /^0b[01]+$/i, ve = /^0o[0-7]+$/i, Ce = parseInt;
function G(e) {
  if (typeof e == "number")
    return e;
  if (ue(e))
    return z;
  if (M(e)) {
    var t = typeof e.valueOf == "function" ? e.valueOf() : e;
    e = M(t) ? t + "" : t;
  }
  if (typeof e != "string")
    return e === 0 ? e : +e;
  e = be(e);
  var n = Ee.test(e);
  return n || ve.test(e) ? Ce(e.slice(2), n ? 2 : 8) : ye.test(e) ? z : +e;
}
var L = function() {
  return de.Date.now();
}, Ie = "Expected a function", Se = Math.max, Re = Math.min;
function Oe(e, t, n) {
  var s, i, r, o, l, a, _ = 0, p = !1, c = !1, g = !0;
  if (typeof e != "function")
    throw new TypeError(Ie);
  t = G(t) || 0, M(n) && (p = !!n.leading, c = "maxWait" in n, r = c ? Se(G(n.maxWait) || 0, t) : r, g = "trailing" in n ? !!n.trailing : g);
  function f(m) {
    var y = s, O = i;
    return s = i = void 0, _ = m, o = e.apply(O, y), o;
  }
  function b(m) {
    return _ = m, l = setTimeout(x, t), p ? f(m) : o;
  }
  function d(m) {
    var y = m - a, O = m - _, V = t - y;
    return c ? Re(V, r - O) : V;
  }
  function w(m) {
    var y = m - a, O = m - _;
    return a === void 0 || y >= t || y < 0 || c && O >= r;
  }
  function x() {
    var m = L();
    if (w(m))
      return C(m);
    l = setTimeout(x, d(m));
  }
  function C(m) {
    return l = void 0, g && s ? f(m) : (s = i = void 0, o);
  }
  function I() {
    l !== void 0 && clearTimeout(l), _ = 0, s = a = i = l = void 0;
  }
  function u() {
    return l === void 0 ? o : C(L());
  }
  function S() {
    var m = L(), y = w(m);
    if (s = arguments, i = this, a = m, y) {
      if (l === void 0)
        return b(a);
      if (c)
        return clearTimeout(l), l = setTimeout(x, t), f(a);
    }
    return l === void 0 && (l = setTimeout(x, t)), o;
  }
  return S.cancel = I, S.flush = u, S;
}
function Te(e, t) {
  return fe(e, t);
}
var re = {
  exports: {}
}, F = {};
/**
 * @license React
 * react-jsx-runtime.production.min.js
 *
 * Copyright (c) Facebook, Inc. and its affiliates.
 *
 * This source code is licensed under the MIT license found in the
 * LICENSE file in the root directory of this source tree.
 */
var Pe = v, je = Symbol.for("react.element"), ke = Symbol.for("react.fragment"), Fe = Object.prototype.hasOwnProperty, Le = Pe.__SECRET_INTERNALS_DO_NOT_USE_OR_YOU_WILL_BE_FIRED.ReactCurrentOwner, Ae = {
  key: !0,
  ref: !0,
  __self: !0,
  __source: !0
};
function oe(e, t, n) {
  var s, i = {}, r = null, o = null;
  n !== void 0 && (r = "" + n), t.key !== void 0 && (r = "" + t.key), t.ref !== void 0 && (o = t.ref);
  for (s in t) Fe.call(t, s) && !Ae.hasOwnProperty(s) && (i[s] = t[s]);
  if (e && e.defaultProps) for (s in t = e.defaultProps, t) i[s] === void 0 && (i[s] = t[s]);
  return {
    $$typeof: je,
    type: e,
    key: r,
    ref: o,
    props: i,
    _owner: Le.current
  };
}
F.Fragment = ke;
F.jsx = oe;
F.jsxs = oe;
re.exports = F;
var h = re.exports;
const {
  SvelteComponent: Ne,
  assign: H,
  binding_callbacks: K,
  check_outros: We,
  children: se,
  claim_element: ie,
  claim_space: Be,
  component_subscribe: J,
  compute_slots: Me,
  create_slot: De,
  detach: R,
  element: le,
  empty: X,
  exclude_internal_props: Y,
  get_all_dirty_from_scope: Ue,
  get_slot_changes: Ve,
  group_outros: qe,
  init: ze,
  insert_hydration: j,
  safe_not_equal: Ge,
  set_custom_element_data: ae,
  space: He,
  transition_in: k,
  transition_out: D,
  update_slot_base: Ke
} = window.__gradio__svelte__internal, {
  beforeUpdate: Je,
  getContext: Xe,
  onDestroy: Ye,
  setContext: Qe
} = window.__gradio__svelte__internal;
function Q(e) {
  let t, n;
  const s = (
    /*#slots*/
    e[7].default
  ), i = De(
    s,
    e,
    /*$$scope*/
    e[6],
    null
  );
  return {
    c() {
      t = le("svelte-slot"), i && i.c(), this.h();
    },
    l(r) {
      t = ie(r, "SVELTE-SLOT", {
        class: !0
      });
      var o = se(t);
      i && i.l(o), o.forEach(R), this.h();
    },
    h() {
      ae(t, "class", "svelte-1rt0kpf");
    },
    m(r, o) {
      j(r, t, o), i && i.m(t, null), e[9](t), n = !0;
    },
    p(r, o) {
      i && i.p && (!n || o & /*$$scope*/
      64) && Ke(
        i,
        s,
        r,
        /*$$scope*/
        r[6],
        n ? Ve(
          s,
          /*$$scope*/
          r[6],
          o,
          null
        ) : Ue(
          /*$$scope*/
          r[6]
        ),
        null
      );
    },
    i(r) {
      n || (k(i, r), n = !0);
    },
    o(r) {
      D(i, r), n = !1;
    },
    d(r) {
      r && R(t), i && i.d(r), e[9](null);
    }
  };
}
function Ze(e) {
  let t, n, s, i, r = (
    /*$$slots*/
    e[4].default && Q(e)
  );
  return {
    c() {
      t = le("react-portal-target"), n = He(), r && r.c(), s = X(), this.h();
    },
    l(o) {
      t = ie(o, "REACT-PORTAL-TARGET", {
        class: !0
      }), se(t).forEach(R), n = Be(o), r && r.l(o), s = X(), this.h();
    },
    h() {
      ae(t, "class", "svelte-1rt0kpf");
    },
    m(o, l) {
      j(o, t, l), e[8](t), j(o, n, l), r && r.m(o, l), j(o, s, l), i = !0;
    },
    p(o, [l]) {
      /*$$slots*/
      o[4].default ? r ? (r.p(o, l), l & /*$$slots*/
      16 && k(r, 1)) : (r = Q(o), r.c(), k(r, 1), r.m(s.parentNode, s)) : r && (qe(), D(r, 1, 1, () => {
        r = null;
      }), We());
    },
    i(o) {
      i || (k(r), i = !0);
    },
    o(o) {
      D(r), i = !1;
    },
    d(o) {
      o && (R(t), R(n), R(s)), e[8](null), r && r.d(o);
    }
  };
}
function Z(e) {
  const {
    svelteInit: t,
    ...n
  } = e;
  return n;
}
function $e(e, t, n) {
  let s, i, {
    $$slots: r = {},
    $$scope: o
  } = t;
  const l = Me(r);
  let {
    svelteInit: a
  } = t;
  const _ = P(Z(t)), p = P();
  J(e, p, (u) => n(0, s = u));
  const c = P();
  J(e, c, (u) => n(1, i = u));
  const g = [], f = Xe("$$ms-gr-react-wrapper"), {
    slotKey: b,
    slotIndex: d,
    subSlotIndex: w
  } = me() || {}, x = a({
    parent: f,
    props: _,
    target: p,
    slot: c,
    slotKey: b,
    slotIndex: d,
    subSlotIndex: w,
    onDestroy(u) {
      g.push(u);
    }
  });
  Qe("$$ms-gr-react-wrapper", x), Je(() => {
    _.set(Z(t));
  }), Ye(() => {
    g.forEach((u) => u());
  });
  function C(u) {
    K[u ? "unshift" : "push"](() => {
      s = u, p.set(s);
    });
  }
  function I(u) {
    K[u ? "unshift" : "push"](() => {
      i = u, c.set(i);
    });
  }
  return e.$$set = (u) => {
    n(17, t = H(H({}, t), Y(u))), "svelteInit" in u && n(5, a = u.svelteInit), "$$scope" in u && n(6, o = u.$$scope);
  }, t = Y(t), [s, i, p, c, l, a, o, r, C, I];
}
class et extends Ne {
  constructor(t) {
    super(), ze(this, t, $e, Ze, Ge, {
      svelteInit: 5
    });
  }
}
const $ = window.ms_globals.rerender, A = window.ms_globals.tree;
function tt(e, t = {}) {
  function n(s) {
    const i = P(), r = new et({
      ...s,
      props: {
        svelteInit(o) {
          window.ms_globals.autokey += 1;
          const l = {
            key: window.ms_globals.autokey,
            svelteInstance: i,
            reactComponent: e,
            props: o.props,
            slot: o.slot,
            target: o.target,
            slotIndex: o.slotIndex,
            subSlotIndex: o.subSlotIndex,
            ignore: t.ignore,
            slotKey: o.slotKey,
            nodes: []
          }, a = o.parent ?? A;
          return a.nodes = [...a.nodes, l], $({
            createPortal: B,
            node: A
          }), o.onDestroy(() => {
            a.nodes = a.nodes.filter((_) => _.svelteInstance !== i), $({
              createPortal: B,
              node: A
            });
          }), l;
        },
        ...s.props
      }
    });
    return i.set(r), r;
  }
  return new Promise((s) => {
    window.ms_globals.initializePromise.then(() => {
      s(n);
    });
  });
}
const nt = ["animationIterationCount", "borderImageOutset", "borderImageSlice", "borderImageWidth", "boxFlex", "boxFlexGroup", "boxOrdinalGroup", "columnCount", "columns", "flex", "flexGrow", "flexPositive", "flexShrink", "flexNegative", "flexOrder", "gridArea", "gridColumn", "gridColumnEnd", "gridColumnStart", "gridRow", "gridRowEnd", "gridRowStart", "lineClamp", "lineHeight", "opacity", "order", "orphans", "tabSize", "widows", "zIndex", "zoom", "fontWeight", "letterSpacing", "lineHeight"];
function rt(e) {
  return e ? Object.keys(e).reduce((t, n) => {
    const s = e[n];
    return t[n] = ot(n, s), t;
  }, {}) : {};
}
function ot(e, t) {
  return typeof t == "number" && !nt.includes(e) ? t + "px" : t;
}
function U(e) {
  const t = [], n = e.cloneNode(!1);
  if (e._reactElement) {
    const i = v.Children.toArray(e._reactElement.props.children).map((r) => {
      if (v.isValidElement(r) && r.props.__slot__) {
        const {
          portals: o,
          clonedElement: l
        } = U(r.props.el);
        return v.cloneElement(r, {
          ...r.props,
          el: l,
          children: [...v.Children.toArray(r.props.children), ...o]
        });
      }
      return null;
    });
    return i.originalChildren = e._reactElement.props.children, t.push(B(v.cloneElement(e._reactElement, {
      ...e._reactElement.props,
      children: i
    }), n)), {
      clonedElement: n,
      portals: t
    };
  }
  Object.keys(e.getEventListeners()).forEach((i) => {
    e.getEventListeners(i).forEach(({
      listener: o,
      type: l,
      useCapture: a
    }) => {
      n.addEventListener(l, o, a);
    });
  });
  const s = Array.from(e.childNodes);
  for (let i = 0; i < s.length; i++) {
    const r = s[i];
    if (r.nodeType === 1) {
      const {
        clonedElement: o,
        portals: l
      } = U(r);
      t.push(...l), n.appendChild(o);
    } else r.nodeType === 3 && n.appendChild(r.cloneNode());
  }
  return {
    clonedElement: n,
    portals: t
  };
}
function st(e, t) {
  e && (typeof e == "function" ? e(t) : e.current = t);
}
const E = ce(({
  slot: e,
  clone: t,
  className: n,
  style: s,
  observeAttributes: i
}, r) => {
  const o = N(), [l, a] = te([]), {
    forceClone: _
  } = pe(), p = _ ? !0 : t;
  return W(() => {
    var b;
    if (!o.current || !e)
      return;
    let c = e;
    function g() {
      let d = c;
      if (c.tagName.toLowerCase() === "svelte-slot" && c.children.length === 1 && c.children[0] && (d = c.children[0], d.tagName.toLowerCase() === "react-portal-target" && d.children[0] && (d = d.children[0])), st(r, d), n && d.classList.add(...n.split(" ")), s) {
        const w = rt(s);
        Object.keys(w).forEach((x) => {
          d.style[x] = w[x];
        });
      }
    }
    let f = null;
    if (p && window.MutationObserver) {
      let d = function() {
        var I, u, S;
        (I = o.current) != null && I.contains(c) && ((u = o.current) == null || u.removeChild(c));
        const {
          portals: x,
          clonedElement: C
        } = U(e);
        c = C, a(x), c.style.display = "contents", g(), (S = o.current) == null || S.appendChild(c);
      };
      d();
      const w = Oe(() => {
        d(), f == null || f.disconnect(), f == null || f.observe(e, {
          childList: !0,
          subtree: !0,
          attributes: i
        });
      }, 50);
      f = new window.MutationObserver(w), f.observe(e, {
        attributes: !0,
        childList: !0,
        subtree: !0
      });
    } else
      c.style.display = "contents", g(), (b = o.current) == null || b.appendChild(c);
    return () => {
      var d, w;
      c.style.display = "", (d = o.current) != null && d.contains(c) && ((w = o.current) == null || w.removeChild(c)), f == null || f.disconnect();
    };
  }, [e, p, n, s, r, i]), v.createElement("react-child", {
    ref: o,
    style: {
      display: "contents"
    }
  }, ...l);
});
function it(e) {
  return /^(?:async\s+)?(?:function\s*(?:\w*\s*)?\(|\([\w\s,=]*\)\s*=>|\(\{[\w\s,=]*\}\)\s*=>|function\s*\*\s*\w*\s*\()/i.test(e.trim());
}
function lt(e, t = !1) {
  try {
    if (_e(e))
      return e;
    if (t && !it(e))
      return;
    if (typeof e == "string") {
      let n = e.trim();
      return n.startsWith(";") && (n = n.slice(1)), n.endsWith(";") && (n = n.slice(0, -1)), new Function(`return (...args) => (${n})(...args)`)();
    }
    return;
  } catch {
    return;
  }
}
function T(e, t) {
  return ne(() => lt(e, t), [e, t]);
}
function at({
  value: e,
  onValueChange: t
}) {
  const [n, s] = te(e), i = N(t);
  i.current = t;
  const r = N(n);
  return r.current = n, W(() => {
    i.current(n);
  }, [n]), W(() => {
    Te(e, r.current) || s(e);
  }, [e]), [n, s];
}
function ct(e) {
  return Object.keys(e).reduce((t, n) => (e[n] !== void 0 && (t[n] = e[n]), t), {});
}
function ee(e, t) {
  return e ? /* @__PURE__ */ h.jsx(E, {
    slot: e,
    clone: t == null ? void 0 : t.clone
  }) : null;
}
function ut({
  key: e,
  slots: t,
  targets: n
}, s) {
  return t[e] ? (...i) => n ? n.map((r, o) => /* @__PURE__ */ h.jsx(q, {
    params: i,
    forceClone: !0,
    children: ee(r, {
      clone: !0,
      ...s
    })
  }, o)) : /* @__PURE__ */ h.jsx(q, {
    params: i,
    forceClone: !0,
    children: ee(t[e], {
      clone: !0,
      ...s
    })
  }) : void 0;
}
const ft = tt(({
  slots: e,
  children: t,
  count: n,
  showCount: s,
  onValueChange: i,
  onChange: r,
  elRef: o,
  setSlotParams: l,
  ...a
}) => {
  const _ = T(n == null ? void 0 : n.strategy), p = T(n == null ? void 0 : n.exceedFormatter), c = T(n == null ? void 0 : n.show), g = T(typeof s == "object" ? s.formatter : void 0), [f, b] = at({
    onValueChange: i,
    value: a.value
  });
  return /* @__PURE__ */ h.jsxs(h.Fragment, {
    children: [/* @__PURE__ */ h.jsx("div", {
      style: {
        display: "none"
      },
      children: t
    }), /* @__PURE__ */ h.jsx(he.Search, {
      ...a,
      value: f,
      ref: o,
      onChange: (d) => {
        r == null || r(d), b(d.target.value);
      },
      showCount: e["showCount.formatter"] ? {
        formatter: ut({
          slots: e,
          setSlotParams: l,
          key: "showCount.formatter"
        })
      } : typeof s == "object" && g ? {
        ...s,
        formatter: g
      } : s,
      count: ne(() => ct({
        ...n,
        exceedFormatter: p,
        strategy: _,
        show: c || (n == null ? void 0 : n.show)
      }), [n, p, _, c]),
      enterButton: e.enterButton ? /* @__PURE__ */ h.jsx(E, {
        slot: e.enterButton
      }) : a.enterButton,
      addonAfter: e.addonAfter ? /* @__PURE__ */ h.jsx(E, {
        slot: e.addonAfter
      }) : a.addonAfter,
      addonBefore: e.addonBefore ? /* @__PURE__ */ h.jsx(E, {
        slot: e.addonBefore
      }) : a.addonBefore,
      allowClear: e["allowClear.clearIcon"] ? {
        clearIcon: /* @__PURE__ */ h.jsx(E, {
          slot: e["allowClear.clearIcon"]
        })
      } : a.allowClear,
      prefix: e.prefix ? /* @__PURE__ */ h.jsx(E, {
        slot: e.prefix
      }) : a.prefix,
      suffix: e.suffix ? /* @__PURE__ */ h.jsx(E, {
        slot: e.suffix
      }) : a.suffix
    })]
  });
});
export {
  ft as InputSearch,
  ft as default
};
