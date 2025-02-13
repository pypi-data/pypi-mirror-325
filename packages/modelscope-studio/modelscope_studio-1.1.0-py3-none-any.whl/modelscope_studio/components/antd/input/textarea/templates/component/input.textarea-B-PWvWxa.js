import { i as ue, a as M, r as de, b as fe, g as me, w as T, c as pe } from "./Index-BBSjyRO8.js";
const E = window.ms_globals.React, ce = window.ms_globals.React.forwardRef, N = window.ms_globals.React.useRef, ee = window.ms_globals.React.useState, A = window.ms_globals.React.useEffect, te = window.ms_globals.React.useMemo, W = window.ms_globals.ReactDOM.createPortal, _e = window.ms_globals.internalContext.useContextPropsContext, q = window.ms_globals.internalContext.ContextPropsProvider, he = window.ms_globals.antd.Input;
var ge = /\s/;
function we(e) {
  for (var t = e.length; t-- && ge.test(e.charAt(t)); )
    ;
  return t;
}
var be = /^\s+/;
function ye(e) {
  return e && e.slice(0, we(e) + 1).replace(be, "");
}
var z = NaN, xe = /^[-+]0x[0-9a-f]+$/i, Ee = /^0b[01]+$/i, ve = /^0o[0-7]+$/i, Ce = parseInt;
function B(e) {
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
  e = ye(e);
  var n = Ee.test(e);
  return n || ve.test(e) ? Ce(e.slice(2), n ? 2 : 8) : xe.test(e) ? z : +e;
}
var j = function() {
  return de.Date.now();
}, Ie = "Expected a function", Se = Math.max, Re = Math.min;
function Oe(e, t, n) {
  var s, i, r, o, l, c, p = 0, _ = !1, a = !1, h = !0;
  if (typeof e != "function")
    throw new TypeError(Ie);
  t = B(t) || 0, M(n) && (_ = !!n.leading, a = "maxWait" in n, r = a ? Se(B(n.maxWait) || 0, t) : r, h = "trailing" in n ? !!n.trailing : h);
  function f(m) {
    var y = s, R = i;
    return s = i = void 0, p = m, o = e.apply(R, y), o;
  }
  function b(m) {
    return p = m, l = setTimeout(w, t), _ ? f(m) : o;
  }
  function d(m) {
    var y = m - c, R = m - p, V = t - y;
    return a ? Re(V, r - R) : V;
  }
  function g(m) {
    var y = m - c, R = m - p;
    return c === void 0 || y >= t || y < 0 || a && R >= r;
  }
  function w() {
    var m = j();
    if (g(m))
      return v(m);
    l = setTimeout(w, d(m));
  }
  function v(m) {
    return l = void 0, h && s ? f(m) : (s = i = void 0, o);
  }
  function C() {
    l !== void 0 && clearTimeout(l), p = 0, s = c = i = l = void 0;
  }
  function u() {
    return l === void 0 ? o : v(j());
  }
  function I() {
    var m = j(), y = g(m);
    if (s = arguments, i = this, c = m, y) {
      if (l === void 0)
        return b(c);
      if (a)
        return clearTimeout(l), l = setTimeout(w, t), f(c);
    }
    return l === void 0 && (l = setTimeout(w, t)), o;
  }
  return I.cancel = C, I.flush = u, I;
}
function Te(e, t) {
  return fe(e, t);
}
var ne = {
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
var Pe = E, ke = Symbol.for("react.element"), Fe = Symbol.for("react.fragment"), je = Object.prototype.hasOwnProperty, Le = Pe.__SECRET_INTERNALS_DO_NOT_USE_OR_YOU_WILL_BE_FIRED.ReactCurrentOwner, Ne = {
  key: !0,
  ref: !0,
  __self: !0,
  __source: !0
};
function re(e, t, n) {
  var s, i = {}, r = null, o = null;
  n !== void 0 && (r = "" + n), t.key !== void 0 && (r = "" + t.key), t.ref !== void 0 && (o = t.ref);
  for (s in t) je.call(t, s) && !Ne.hasOwnProperty(s) && (i[s] = t[s]);
  if (e && e.defaultProps) for (s in t = e.defaultProps, t) i[s] === void 0 && (i[s] = t[s]);
  return {
    $$typeof: ke,
    type: e,
    key: r,
    ref: o,
    props: i,
    _owner: Le.current
  };
}
F.Fragment = Fe;
F.jsx = re;
F.jsxs = re;
ne.exports = F;
var x = ne.exports;
const {
  SvelteComponent: Ae,
  assign: G,
  binding_callbacks: H,
  check_outros: We,
  children: oe,
  claim_element: se,
  claim_space: Me,
  component_subscribe: K,
  compute_slots: De,
  create_slot: Ue,
  detach: S,
  element: ie,
  empty: J,
  exclude_internal_props: X,
  get_all_dirty_from_scope: Ve,
  get_slot_changes: qe,
  group_outros: ze,
  init: Be,
  insert_hydration: P,
  safe_not_equal: Ge,
  set_custom_element_data: le,
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
function Y(e) {
  let t, n;
  const s = (
    /*#slots*/
    e[7].default
  ), i = Ue(
    s,
    e,
    /*$$scope*/
    e[6],
    null
  );
  return {
    c() {
      t = ie("svelte-slot"), i && i.c(), this.h();
    },
    l(r) {
      t = se(r, "SVELTE-SLOT", {
        class: !0
      });
      var o = oe(t);
      i && i.l(o), o.forEach(S), this.h();
    },
    h() {
      le(t, "class", "svelte-1rt0kpf");
    },
    m(r, o) {
      P(r, t, o), i && i.m(t, null), e[9](t), n = !0;
    },
    p(r, o) {
      i && i.p && (!n || o & /*$$scope*/
      64) && Ke(
        i,
        s,
        r,
        /*$$scope*/
        r[6],
        n ? qe(
          s,
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
      n || (k(i, r), n = !0);
    },
    o(r) {
      D(i, r), n = !1;
    },
    d(r) {
      r && S(t), i && i.d(r), e[9](null);
    }
  };
}
function Ze(e) {
  let t, n, s, i, r = (
    /*$$slots*/
    e[4].default && Y(e)
  );
  return {
    c() {
      t = ie("react-portal-target"), n = He(), r && r.c(), s = J(), this.h();
    },
    l(o) {
      t = se(o, "REACT-PORTAL-TARGET", {
        class: !0
      }), oe(t).forEach(S), n = Me(o), r && r.l(o), s = J(), this.h();
    },
    h() {
      le(t, "class", "svelte-1rt0kpf");
    },
    m(o, l) {
      P(o, t, l), e[8](t), P(o, n, l), r && r.m(o, l), P(o, s, l), i = !0;
    },
    p(o, [l]) {
      /*$$slots*/
      o[4].default ? r ? (r.p(o, l), l & /*$$slots*/
      16 && k(r, 1)) : (r = Y(o), r.c(), k(r, 1), r.m(s.parentNode, s)) : r && (ze(), D(r, 1, 1, () => {
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
      o && (S(t), S(n), S(s)), e[8](null), r && r.d(o);
    }
  };
}
function Q(e) {
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
  const l = De(r);
  let {
    svelteInit: c
  } = t;
  const p = T(Q(t)), _ = T();
  K(e, _, (u) => n(0, s = u));
  const a = T();
  K(e, a, (u) => n(1, i = u));
  const h = [], f = Xe("$$ms-gr-react-wrapper"), {
    slotKey: b,
    slotIndex: d,
    subSlotIndex: g
  } = me() || {}, w = c({
    parent: f,
    props: p,
    target: _,
    slot: a,
    slotKey: b,
    slotIndex: d,
    subSlotIndex: g,
    onDestroy(u) {
      h.push(u);
    }
  });
  Qe("$$ms-gr-react-wrapper", w), Je(() => {
    p.set(Q(t));
  }), Ye(() => {
    h.forEach((u) => u());
  });
  function v(u) {
    H[u ? "unshift" : "push"](() => {
      s = u, _.set(s);
    });
  }
  function C(u) {
    H[u ? "unshift" : "push"](() => {
      i = u, a.set(i);
    });
  }
  return e.$$set = (u) => {
    n(17, t = G(G({}, t), X(u))), "svelteInit" in u && n(5, c = u.svelteInit), "$$scope" in u && n(6, o = u.$$scope);
  }, t = X(t), [s, i, _, a, l, c, o, r, v, C];
}
class et extends Ae {
  constructor(t) {
    super(), Be(this, t, $e, Ze, Ge, {
      svelteInit: 5
    });
  }
}
const Z = window.ms_globals.rerender, L = window.ms_globals.tree;
function tt(e, t = {}) {
  function n(s) {
    const i = T(), r = new et({
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
          }, c = o.parent ?? L;
          return c.nodes = [...c.nodes, l], Z({
            createPortal: W,
            node: L
          }), o.onDestroy(() => {
            c.nodes = c.nodes.filter((p) => p.svelteInstance !== i), Z({
              createPortal: W,
              node: L
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
    const i = E.Children.toArray(e._reactElement.props.children).map((r) => {
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
    return i.originalChildren = e._reactElement.props.children, t.push(W(E.cloneElement(e._reactElement, {
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
      useCapture: c
    }) => {
      n.addEventListener(l, o, c);
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
const ae = ce(({
  slot: e,
  clone: t,
  className: n,
  style: s,
  observeAttributes: i
}, r) => {
  const o = N(), [l, c] = ee([]), {
    forceClone: p
  } = _e(), _ = p ? !0 : t;
  return A(() => {
    var b;
    if (!o.current || !e)
      return;
    let a = e;
    function h() {
      let d = a;
      if (a.tagName.toLowerCase() === "svelte-slot" && a.children.length === 1 && a.children[0] && (d = a.children[0], d.tagName.toLowerCase() === "react-portal-target" && d.children[0] && (d = d.children[0])), st(r, d), n && d.classList.add(...n.split(" ")), s) {
        const g = rt(s);
        Object.keys(g).forEach((w) => {
          d.style[w] = g[w];
        });
      }
    }
    let f = null;
    if (_ && window.MutationObserver) {
      let d = function() {
        var C, u, I;
        (C = o.current) != null && C.contains(a) && ((u = o.current) == null || u.removeChild(a));
        const {
          portals: w,
          clonedElement: v
        } = U(e);
        a = v, c(w), a.style.display = "contents", h(), (I = o.current) == null || I.appendChild(a);
      };
      d();
      const g = Oe(() => {
        d(), f == null || f.disconnect(), f == null || f.observe(e, {
          childList: !0,
          subtree: !0,
          attributes: i
        });
      }, 50);
      f = new window.MutationObserver(g), f.observe(e, {
        attributes: !0,
        childList: !0,
        subtree: !0
      });
    } else
      a.style.display = "contents", h(), (b = o.current) == null || b.appendChild(a);
    return () => {
      var d, g;
      a.style.display = "", (d = o.current) != null && d.contains(a) && ((g = o.current) == null || g.removeChild(a)), f == null || f.disconnect();
    };
  }, [e, _, n, s, r, i]), E.createElement("react-child", {
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
    if (pe(e))
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
function O(e, t) {
  return te(() => lt(e, t), [e, t]);
}
function at({
  value: e,
  onValueChange: t
}) {
  const [n, s] = ee(e), i = N(t);
  i.current = t;
  const r = N(n);
  return r.current = n, A(() => {
    i.current(n);
  }, [n]), A(() => {
    Te(e, r.current) || s(e);
  }, [e]), [n, s];
}
function ct(e) {
  return Object.keys(e).reduce((t, n) => (e[n] !== void 0 && (t[n] = e[n]), t), {});
}
function $(e, t) {
  return e ? /* @__PURE__ */ x.jsx(ae, {
    slot: e,
    clone: t == null ? void 0 : t.clone
  }) : null;
}
function ut({
  key: e,
  slots: t,
  targets: n
}, s) {
  return t[e] ? (...i) => n ? n.map((r, o) => /* @__PURE__ */ x.jsx(q, {
    params: i,
    forceClone: !0,
    children: $(r, {
      clone: !0,
      ...s
    })
  }, o)) : /* @__PURE__ */ x.jsx(q, {
    params: i,
    forceClone: !0,
    children: $(t[e], {
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
  ...c
}) => {
  const p = O(n == null ? void 0 : n.strategy), _ = O(n == null ? void 0 : n.exceedFormatter), a = O(n == null ? void 0 : n.show), h = O(typeof s == "object" ? s.formatter : void 0), [f, b] = at({
    onValueChange: i,
    value: c.value
  });
  return /* @__PURE__ */ x.jsxs(x.Fragment, {
    children: [/* @__PURE__ */ x.jsx("div", {
      style: {
        display: "none"
      },
      children: t
    }), /* @__PURE__ */ x.jsx(he.TextArea, {
      ...c,
      ref: o,
      value: f,
      onChange: (d) => {
        r == null || r(d), b(d.target.value);
      },
      showCount: e["showCount.formatter"] ? {
        formatter: ut({
          slots: e,
          setSlotParams: l,
          key: "showCount.formatter"
        })
      } : typeof s == "object" && h ? {
        ...s,
        formatter: h
      } : s,
      count: te(() => ct({
        ...n,
        exceedFormatter: _,
        strategy: p,
        show: a || (n == null ? void 0 : n.show)
      }), [n, _, p, a]),
      allowClear: e["allowClear.clearIcon"] ? {
        clearIcon: /* @__PURE__ */ x.jsx(ae, {
          slot: e["allowClear.clearIcon"]
        })
      } : c.allowClear
    })]
  });
});
export {
  ft as InputTextarea,
  ft as default
};
