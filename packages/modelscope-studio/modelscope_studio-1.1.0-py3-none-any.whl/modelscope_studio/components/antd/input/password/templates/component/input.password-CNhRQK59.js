import { i as de, a as B, r as fe, b as me, g as _e, w as T, c as pe } from "./Index-BM_waRqV.js";
const E = window.ms_globals.React, ue = window.ms_globals.React.forwardRef, N = window.ms_globals.React.useRef, ne = window.ms_globals.React.useState, W = window.ms_globals.React.useEffect, re = window.ms_globals.React.useMemo, M = window.ms_globals.ReactDOM.createPortal, he = window.ms_globals.internalContext.useContextPropsContext, q = window.ms_globals.internalContext.ContextPropsProvider, ge = window.ms_globals.antd.Input;
var we = /\s/;
function xe(e) {
  for (var t = e.length; t-- && we.test(e.charAt(t)); )
    ;
  return t;
}
var ye = /^\s+/;
function be(e) {
  return e && e.slice(0, xe(e) + 1).replace(ye, "");
}
var z = NaN, Ee = /^[-+]0x[0-9a-f]+$/i, ve = /^0b[01]+$/i, Ce = /^0o[0-7]+$/i, Ie = parseInt;
function G(e) {
  if (typeof e == "number")
    return e;
  if (de(e))
    return z;
  if (B(e)) {
    var t = typeof e.valueOf == "function" ? e.valueOf() : e;
    e = B(t) ? t + "" : t;
  }
  if (typeof e != "string")
    return e === 0 ? e : +e;
  e = be(e);
  var n = ve.test(e);
  return n || Ce.test(e) ? Ie(e.slice(2), n ? 2 : 8) : Ee.test(e) ? z : +e;
}
var L = function() {
  return fe.Date.now();
}, Re = "Expected a function", Se = Math.max, Oe = Math.min;
function Pe(e, t, n) {
  var i, s, r, o, l, u, d = 0, g = !1, a = !1, w = !0;
  if (typeof e != "function")
    throw new TypeError(Re);
  t = G(t) || 0, B(n) && (g = !!n.leading, a = "maxWait" in n, r = a ? Se(G(n.maxWait) || 0, t) : r, w = "trailing" in n ? !!n.trailing : w);
  function f(_) {
    var b = i, O = s;
    return i = s = void 0, d = _, o = e.apply(O, b), o;
  }
  function y(_) {
    return d = _, l = setTimeout(h, t), g ? f(_) : o;
  }
  function m(_) {
    var b = _ - u, O = _ - d, V = t - b;
    return a ? Oe(V, r - O) : V;
  }
  function p(_) {
    var b = _ - u, O = _ - d;
    return u === void 0 || b >= t || b < 0 || a && O >= r;
  }
  function h() {
    var _ = L();
    if (p(_))
      return v(_);
    l = setTimeout(h, m(_));
  }
  function v(_) {
    return l = void 0, w && i ? f(_) : (i = s = void 0, o);
  }
  function C() {
    l !== void 0 && clearTimeout(l), d = 0, i = u = s = l = void 0;
  }
  function c() {
    return l === void 0 ? o : v(L());
  }
  function I() {
    var _ = L(), b = p(_);
    if (i = arguments, s = this, u = _, b) {
      if (l === void 0)
        return y(u);
      if (a)
        return clearTimeout(l), l = setTimeout(h, t), f(u);
    }
    return l === void 0 && (l = setTimeout(h, t)), o;
  }
  return I.cancel = C, I.flush = c, I;
}
function Te(e, t) {
  return me(e, t);
}
var oe = {
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
var ke = E, je = Symbol.for("react.element"), Fe = Symbol.for("react.fragment"), Le = Object.prototype.hasOwnProperty, Ae = ke.__SECRET_INTERNALS_DO_NOT_USE_OR_YOU_WILL_BE_FIRED.ReactCurrentOwner, Ne = {
  key: !0,
  ref: !0,
  __self: !0,
  __source: !0
};
function ie(e, t, n) {
  var i, s = {}, r = null, o = null;
  n !== void 0 && (r = "" + n), t.key !== void 0 && (r = "" + t.key), t.ref !== void 0 && (o = t.ref);
  for (i in t) Le.call(t, i) && !Ne.hasOwnProperty(i) && (s[i] = t[i]);
  if (e && e.defaultProps) for (i in t = e.defaultProps, t) s[i] === void 0 && (s[i] = t[i]);
  return {
    $$typeof: je,
    type: e,
    key: r,
    ref: o,
    props: s,
    _owner: Ae.current
  };
}
F.Fragment = Fe;
F.jsx = ie;
F.jsxs = ie;
oe.exports = F;
var x = oe.exports;
const {
  SvelteComponent: We,
  assign: H,
  binding_callbacks: K,
  check_outros: Me,
  children: se,
  claim_element: le,
  claim_space: Be,
  component_subscribe: J,
  compute_slots: De,
  create_slot: Ue,
  detach: S,
  element: ae,
  empty: X,
  exclude_internal_props: Y,
  get_all_dirty_from_scope: Ve,
  get_slot_changes: qe,
  group_outros: ze,
  init: Ge,
  insert_hydration: k,
  safe_not_equal: He,
  set_custom_element_data: ce,
  space: Ke,
  transition_in: j,
  transition_out: D,
  update_slot_base: Je
} = window.__gradio__svelte__internal, {
  beforeUpdate: Xe,
  getContext: Ye,
  onDestroy: Qe,
  setContext: Ze
} = window.__gradio__svelte__internal;
function Q(e) {
  let t, n;
  const i = (
    /*#slots*/
    e[7].default
  ), s = Ue(
    i,
    e,
    /*$$scope*/
    e[6],
    null
  );
  return {
    c() {
      t = ae("svelte-slot"), s && s.c(), this.h();
    },
    l(r) {
      t = le(r, "SVELTE-SLOT", {
        class: !0
      });
      var o = se(t);
      s && s.l(o), o.forEach(S), this.h();
    },
    h() {
      ce(t, "class", "svelte-1rt0kpf");
    },
    m(r, o) {
      k(r, t, o), s && s.m(t, null), e[9](t), n = !0;
    },
    p(r, o) {
      s && s.p && (!n || o & /*$$scope*/
      64) && Je(
        s,
        i,
        r,
        /*$$scope*/
        r[6],
        n ? qe(
          i,
          /*$$scope*/
          r[6],
          o,
          null
        ) : Ve(
          /*$$scope*/
          r[6]
        ),
        null
      );
    },
    i(r) {
      n || (j(s, r), n = !0);
    },
    o(r) {
      D(s, r), n = !1;
    },
    d(r) {
      r && S(t), s && s.d(r), e[9](null);
    }
  };
}
function $e(e) {
  let t, n, i, s, r = (
    /*$$slots*/
    e[4].default && Q(e)
  );
  return {
    c() {
      t = ae("react-portal-target"), n = Ke(), r && r.c(), i = X(), this.h();
    },
    l(o) {
      t = le(o, "REACT-PORTAL-TARGET", {
        class: !0
      }), se(t).forEach(S), n = Be(o), r && r.l(o), i = X(), this.h();
    },
    h() {
      ce(t, "class", "svelte-1rt0kpf");
    },
    m(o, l) {
      k(o, t, l), e[8](t), k(o, n, l), r && r.m(o, l), k(o, i, l), s = !0;
    },
    p(o, [l]) {
      /*$$slots*/
      o[4].default ? r ? (r.p(o, l), l & /*$$slots*/
      16 && j(r, 1)) : (r = Q(o), r.c(), j(r, 1), r.m(i.parentNode, i)) : r && (ze(), D(r, 1, 1, () => {
        r = null;
      }), Me());
    },
    i(o) {
      s || (j(r), s = !0);
    },
    o(o) {
      D(r), s = !1;
    },
    d(o) {
      o && (S(t), S(n), S(i)), e[8](null), r && r.d(o);
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
function et(e, t, n) {
  let i, s, {
    $$slots: r = {},
    $$scope: o
  } = t;
  const l = De(r);
  let {
    svelteInit: u
  } = t;
  const d = T(Z(t)), g = T();
  J(e, g, (c) => n(0, i = c));
  const a = T();
  J(e, a, (c) => n(1, s = c));
  const w = [], f = Ye("$$ms-gr-react-wrapper"), {
    slotKey: y,
    slotIndex: m,
    subSlotIndex: p
  } = _e() || {}, h = u({
    parent: f,
    props: d,
    target: g,
    slot: a,
    slotKey: y,
    slotIndex: m,
    subSlotIndex: p,
    onDestroy(c) {
      w.push(c);
    }
  });
  Ze("$$ms-gr-react-wrapper", h), Xe(() => {
    d.set(Z(t));
  }), Qe(() => {
    w.forEach((c) => c());
  });
  function v(c) {
    K[c ? "unshift" : "push"](() => {
      i = c, g.set(i);
    });
  }
  function C(c) {
    K[c ? "unshift" : "push"](() => {
      s = c, a.set(s);
    });
  }
  return e.$$set = (c) => {
    n(17, t = H(H({}, t), Y(c))), "svelteInit" in c && n(5, u = c.svelteInit), "$$scope" in c && n(6, o = c.$$scope);
  }, t = Y(t), [i, s, g, a, l, u, o, r, v, C];
}
class tt extends We {
  constructor(t) {
    super(), Ge(this, t, et, $e, He, {
      svelteInit: 5
    });
  }
}
const $ = window.ms_globals.rerender, A = window.ms_globals.tree;
function nt(e, t = {}) {
  function n(i) {
    const s = T(), r = new tt({
      ...i,
      props: {
        svelteInit(o) {
          window.ms_globals.autokey += 1;
          const l = {
            key: window.ms_globals.autokey,
            svelteInstance: s,
            reactComponent: e,
            props: o.props,
            slot: o.slot,
            target: o.target,
            slotIndex: o.slotIndex,
            subSlotIndex: o.subSlotIndex,
            ignore: t.ignore,
            slotKey: o.slotKey,
            nodes: []
          }, u = o.parent ?? A;
          return u.nodes = [...u.nodes, l], $({
            createPortal: M,
            node: A
          }), o.onDestroy(() => {
            u.nodes = u.nodes.filter((d) => d.svelteInstance !== s), $({
              createPortal: M,
              node: A
            });
          }), l;
        },
        ...i.props
      }
    });
    return s.set(r), r;
  }
  return new Promise((i) => {
    window.ms_globals.initializePromise.then(() => {
      i(n);
    });
  });
}
const rt = ["animationIterationCount", "borderImageOutset", "borderImageSlice", "borderImageWidth", "boxFlex", "boxFlexGroup", "boxOrdinalGroup", "columnCount", "columns", "flex", "flexGrow", "flexPositive", "flexShrink", "flexNegative", "flexOrder", "gridArea", "gridColumn", "gridColumnEnd", "gridColumnStart", "gridRow", "gridRowEnd", "gridRowStart", "lineClamp", "lineHeight", "opacity", "order", "orphans", "tabSize", "widows", "zIndex", "zoom", "fontWeight", "letterSpacing", "lineHeight"];
function ot(e) {
  return e ? Object.keys(e).reduce((t, n) => {
    const i = e[n];
    return t[n] = it(n, i), t;
  }, {}) : {};
}
function it(e, t) {
  return typeof t == "number" && !rt.includes(e) ? t + "px" : t;
}
function U(e) {
  const t = [], n = e.cloneNode(!1);
  if (e._reactElement) {
    const s = E.Children.toArray(e._reactElement.props.children).map((r) => {
      if (E.isValidElement(r) && r.props.__slot__) {
        const {
          portals: o,
          clonedElement: l
        } = U(r.props.el);
        return E.cloneElement(r, {
          ...r.props,
          el: l,
          children: [...E.Children.toArray(r.props.children), ...o]
        });
      }
      return null;
    });
    return s.originalChildren = e._reactElement.props.children, t.push(M(E.cloneElement(e._reactElement, {
      ...e._reactElement.props,
      children: s
    }), n)), {
      clonedElement: n,
      portals: t
    };
  }
  Object.keys(e.getEventListeners()).forEach((s) => {
    e.getEventListeners(s).forEach(({
      listener: o,
      type: l,
      useCapture: u
    }) => {
      n.addEventListener(l, o, u);
    });
  });
  const i = Array.from(e.childNodes);
  for (let s = 0; s < i.length; s++) {
    const r = i[s];
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
const R = ue(({
  slot: e,
  clone: t,
  className: n,
  style: i,
  observeAttributes: s
}, r) => {
  const o = N(), [l, u] = ne([]), {
    forceClone: d
  } = he(), g = d ? !0 : t;
  return W(() => {
    var y;
    if (!o.current || !e)
      return;
    let a = e;
    function w() {
      let m = a;
      if (a.tagName.toLowerCase() === "svelte-slot" && a.children.length === 1 && a.children[0] && (m = a.children[0], m.tagName.toLowerCase() === "react-portal-target" && m.children[0] && (m = m.children[0])), st(r, m), n && m.classList.add(...n.split(" ")), i) {
        const p = ot(i);
        Object.keys(p).forEach((h) => {
          m.style[h] = p[h];
        });
      }
    }
    let f = null;
    if (g && window.MutationObserver) {
      let m = function() {
        var C, c, I;
        (C = o.current) != null && C.contains(a) && ((c = o.current) == null || c.removeChild(a));
        const {
          portals: h,
          clonedElement: v
        } = U(e);
        a = v, u(h), a.style.display = "contents", w(), (I = o.current) == null || I.appendChild(a);
      };
      m();
      const p = Pe(() => {
        m(), f == null || f.disconnect(), f == null || f.observe(e, {
          childList: !0,
          subtree: !0,
          attributes: s
        });
      }, 50);
      f = new window.MutationObserver(p), f.observe(e, {
        attributes: !0,
        childList: !0,
        subtree: !0
      });
    } else
      a.style.display = "contents", w(), (y = o.current) == null || y.appendChild(a);
    return () => {
      var m, p;
      a.style.display = "", (m = o.current) != null && m.contains(a) && ((p = o.current) == null || p.removeChild(a)), f == null || f.disconnect();
    };
  }, [e, g, n, i, r, s]), E.createElement("react-child", {
    ref: o,
    style: {
      display: "contents"
    }
  }, ...l);
});
function lt(e) {
  return /^(?:async\s+)?(?:function\s*(?:\w*\s*)?\(|\([\w\s,=]*\)\s*=>|\(\{[\w\s,=]*\}\)\s*=>|function\s*\*\s*\w*\s*\()/i.test(e.trim());
}
function at(e, t = !1) {
  try {
    if (pe(e))
      return e;
    if (t && !lt(e))
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
function P(e, t) {
  return re(() => at(e, t), [e, t]);
}
function ct({
  value: e,
  onValueChange: t
}) {
  const [n, i] = ne(e), s = N(t);
  s.current = t;
  const r = N(n);
  return r.current = n, W(() => {
    s.current(n);
  }, [n]), W(() => {
    Te(e, r.current) || i(e);
  }, [e]), [n, i];
}
function ut(e) {
  return Object.keys(e).reduce((t, n) => (e[n] !== void 0 && (t[n] = e[n]), t), {});
}
function ee(e, t) {
  return e ? /* @__PURE__ */ x.jsx(R, {
    slot: e,
    clone: t == null ? void 0 : t.clone
  }) : null;
}
function te({
  key: e,
  slots: t,
  targets: n
}, i) {
  return t[e] ? (...s) => n ? n.map((r, o) => /* @__PURE__ */ x.jsx(q, {
    params: s,
    forceClone: !0,
    children: ee(r, {
      clone: !0,
      ...i
    })
  }, o)) : /* @__PURE__ */ x.jsx(q, {
    params: s,
    forceClone: !0,
    children: ee(t[e], {
      clone: !0,
      ...i
    })
  }) : void 0;
}
const ft = nt(({
  slots: e,
  children: t,
  count: n,
  showCount: i,
  onValueChange: s,
  onChange: r,
  iconRender: o,
  elRef: l,
  setSlotParams: u,
  ...d
}) => {
  const g = P(n == null ? void 0 : n.strategy), a = P(n == null ? void 0 : n.exceedFormatter), w = P(n == null ? void 0 : n.show), f = P(typeof i == "object" ? i.formatter : void 0), y = P(o), [m, p] = ct({
    onValueChange: s,
    value: d.value
  });
  return /* @__PURE__ */ x.jsxs(x.Fragment, {
    children: [/* @__PURE__ */ x.jsx("div", {
      style: {
        display: "none"
      },
      children: t
    }), /* @__PURE__ */ x.jsx(ge.Password, {
      ...d,
      value: m,
      ref: l,
      onChange: (h) => {
        r == null || r(h), p(h.target.value);
      },
      iconRender: e.iconRender ? te({
        slots: e,
        setSlotParams: u,
        key: "iconRender"
      }) : y,
      showCount: e["showCount.formatter"] ? {
        formatter: te({
          slots: e,
          setSlotParams: u,
          key: "showCount.formatter"
        })
      } : typeof i == "object" && f ? {
        ...i,
        formatter: f
      } : i,
      count: re(() => ut({
        ...n,
        exceedFormatter: a,
        strategy: g,
        show: w || (n == null ? void 0 : n.show)
      }), [n, a, g, w]),
      addonAfter: e.addonAfter ? /* @__PURE__ */ x.jsx(R, {
        slot: e.addonAfter
      }) : d.addonAfter,
      addonBefore: e.addonBefore ? /* @__PURE__ */ x.jsx(R, {
        slot: e.addonBefore
      }) : d.addonBefore,
      allowClear: e["allowClear.clearIcon"] ? {
        clearIcon: /* @__PURE__ */ x.jsx(R, {
          slot: e["allowClear.clearIcon"]
        })
      } : d.allowClear,
      prefix: e.prefix ? /* @__PURE__ */ x.jsx(R, {
        slot: e.prefix
      }) : d.prefix,
      suffix: e.suffix ? /* @__PURE__ */ x.jsx(R, {
        slot: e.suffix
      }) : d.suffix
    })]
  });
});
export {
  ft as InputPassword,
  ft as default
};
