import { i as pe, a as M, r as me, g as _e, w as L, d as ge, b as T, c as he } from "./Index-Cd9C3r6q.js";
const E = window.ms_globals.React, B = window.ms_globals.React.useMemo, re = window.ms_globals.React.useState, oe = window.ms_globals.React.useEffect, de = window.ms_globals.React.forwardRef, fe = window.ms_globals.React.useRef, W = window.ms_globals.ReactDOM.createPortal, be = window.ms_globals.internalContext.useContextPropsContext, G = window.ms_globals.internalContext.ContextPropsProvider, xe = window.ms_globals.antd.Transfer;
var we = /\s/;
function ye(e) {
  for (var t = e.length; t-- && we.test(e.charAt(t)); )
    ;
  return t;
}
var ve = /^\s+/;
function Ee(e) {
  return e && e.slice(0, ye(e) + 1).replace(ve, "");
}
var H = NaN, Ie = /^[-+]0x[0-9a-f]+$/i, Ce = /^0b[01]+$/i, Se = /^0o[0-7]+$/i, Re = parseInt;
function V(e) {
  if (typeof e == "number")
    return e;
  if (pe(e))
    return H;
  if (M(e)) {
    var t = typeof e.valueOf == "function" ? e.valueOf() : e;
    e = M(t) ? t + "" : t;
  }
  if (typeof e != "string")
    return e === 0 ? e : +e;
  e = Ee(e);
  var o = Ce.test(e);
  return o || Se.test(e) ? Re(e.slice(2), o ? 2 : 8) : Ie.test(e) ? H : +e;
}
var A = function() {
  return me.Date.now();
}, Te = "Expected a function", Oe = Math.max, ke = Math.min;
function Le(e, t, o) {
  var l, s, n, r, i, a, _ = 0, g = !1, c = !1, b = !0;
  if (typeof e != "function")
    throw new TypeError(Te);
  t = V(t) || 0, M(o) && (g = !!o.leading, c = "maxWait" in o, n = c ? Oe(V(o.maxWait) || 0, t) : n, b = "trailing" in o ? !!o.trailing : b);
  function p(m) {
    var v = l, R = s;
    return l = s = void 0, _ = m, r = e.apply(R, v), r;
  }
  function y(m) {
    return _ = m, i = setTimeout(u, t), g ? p(m) : r;
  }
  function f(m) {
    var v = m - a, R = m - _, z = t - v;
    return c ? ke(z, n - R) : z;
  }
  function h(m) {
    var v = m - a, R = m - _;
    return a === void 0 || v >= t || v < 0 || c && R >= n;
  }
  function u() {
    var m = A();
    if (h(m))
      return x(m);
    i = setTimeout(u, f(m));
  }
  function x(m) {
    return i = void 0, b && l ? p(m) : (l = s = void 0, r);
  }
  function I() {
    i !== void 0 && clearTimeout(i), _ = 0, l = a = s = i = void 0;
  }
  function d() {
    return i === void 0 ? r : x(A());
  }
  function C() {
    var m = A(), v = h(m);
    if (l = arguments, s = this, a = m, v) {
      if (i === void 0)
        return y(a);
      if (c)
        return clearTimeout(i), i = setTimeout(u, t), p(a);
    }
    return i === void 0 && (i = setTimeout(u, t)), r;
  }
  return C.cancel = I, C.flush = d, C;
}
var se = {
  exports: {}
}, j = {};
/**
 * @license React
 * react-jsx-runtime.production.min.js
 *
 * Copyright (c) Facebook, Inc. and its affiliates.
 *
 * This source code is licensed under the MIT license found in the
 * LICENSE file in the root directory of this source tree.
 */
var Pe = E, Fe = Symbol.for("react.element"), je = Symbol.for("react.fragment"), Ae = Object.prototype.hasOwnProperty, Ne = Pe.__SECRET_INTERNALS_DO_NOT_USE_OR_YOU_WILL_BE_FIRED.ReactCurrentOwner, We = {
  key: !0,
  ref: !0,
  __self: !0,
  __source: !0
};
function le(e, t, o) {
  var l, s = {}, n = null, r = null;
  o !== void 0 && (n = "" + o), t.key !== void 0 && (n = "" + t.key), t.ref !== void 0 && (r = t.ref);
  for (l in t) Ae.call(t, l) && !We.hasOwnProperty(l) && (s[l] = t[l]);
  if (e && e.defaultProps) for (l in t = e.defaultProps, t) s[l] === void 0 && (s[l] = t[l]);
  return {
    $$typeof: Fe,
    type: e,
    key: n,
    ref: r,
    props: s,
    _owner: Ne.current
  };
}
j.Fragment = je;
j.jsx = le;
j.jsxs = le;
se.exports = j;
var w = se.exports;
const {
  SvelteComponent: Me,
  assign: q,
  binding_callbacks: J,
  check_outros: De,
  children: ie,
  claim_element: ce,
  claim_space: Ue,
  component_subscribe: K,
  compute_slots: Be,
  create_slot: ze,
  detach: S,
  element: ae,
  empty: X,
  exclude_internal_props: Y,
  get_all_dirty_from_scope: Ge,
  get_slot_changes: He,
  group_outros: Ve,
  init: qe,
  insert_hydration: P,
  safe_not_equal: Je,
  set_custom_element_data: ue,
  space: Ke,
  transition_in: F,
  transition_out: D,
  update_slot_base: Xe
} = window.__gradio__svelte__internal, {
  beforeUpdate: Ye,
  getContext: Qe,
  onDestroy: Ze,
  setContext: $e
} = window.__gradio__svelte__internal;
function Q(e) {
  let t, o;
  const l = (
    /*#slots*/
    e[7].default
  ), s = ze(
    l,
    e,
    /*$$scope*/
    e[6],
    null
  );
  return {
    c() {
      t = ae("svelte-slot"), s && s.c(), this.h();
    },
    l(n) {
      t = ce(n, "SVELTE-SLOT", {
        class: !0
      });
      var r = ie(t);
      s && s.l(r), r.forEach(S), this.h();
    },
    h() {
      ue(t, "class", "svelte-1rt0kpf");
    },
    m(n, r) {
      P(n, t, r), s && s.m(t, null), e[9](t), o = !0;
    },
    p(n, r) {
      s && s.p && (!o || r & /*$$scope*/
      64) && Xe(
        s,
        l,
        n,
        /*$$scope*/
        n[6],
        o ? He(
          l,
          /*$$scope*/
          n[6],
          r,
          null
        ) : Ge(
          /*$$scope*/
          n[6]
        ),
        null
      );
    },
    i(n) {
      o || (F(s, n), o = !0);
    },
    o(n) {
      D(s, n), o = !1;
    },
    d(n) {
      n && S(t), s && s.d(n), e[9](null);
    }
  };
}
function et(e) {
  let t, o, l, s, n = (
    /*$$slots*/
    e[4].default && Q(e)
  );
  return {
    c() {
      t = ae("react-portal-target"), o = Ke(), n && n.c(), l = X(), this.h();
    },
    l(r) {
      t = ce(r, "REACT-PORTAL-TARGET", {
        class: !0
      }), ie(t).forEach(S), o = Ue(r), n && n.l(r), l = X(), this.h();
    },
    h() {
      ue(t, "class", "svelte-1rt0kpf");
    },
    m(r, i) {
      P(r, t, i), e[8](t), P(r, o, i), n && n.m(r, i), P(r, l, i), s = !0;
    },
    p(r, [i]) {
      /*$$slots*/
      r[4].default ? n ? (n.p(r, i), i & /*$$slots*/
      16 && F(n, 1)) : (n = Q(r), n.c(), F(n, 1), n.m(l.parentNode, l)) : n && (Ve(), D(n, 1, 1, () => {
        n = null;
      }), De());
    },
    i(r) {
      s || (F(n), s = !0);
    },
    o(r) {
      D(n), s = !1;
    },
    d(r) {
      r && (S(t), S(o), S(l)), e[8](null), n && n.d(r);
    }
  };
}
function Z(e) {
  const {
    svelteInit: t,
    ...o
  } = e;
  return o;
}
function tt(e, t, o) {
  let l, s, {
    $$slots: n = {},
    $$scope: r
  } = t;
  const i = Be(n);
  let {
    svelteInit: a
  } = t;
  const _ = L(Z(t)), g = L();
  K(e, g, (d) => o(0, l = d));
  const c = L();
  K(e, c, (d) => o(1, s = d));
  const b = [], p = Qe("$$ms-gr-react-wrapper"), {
    slotKey: y,
    slotIndex: f,
    subSlotIndex: h
  } = _e() || {}, u = a({
    parent: p,
    props: _,
    target: g,
    slot: c,
    slotKey: y,
    slotIndex: f,
    subSlotIndex: h,
    onDestroy(d) {
      b.push(d);
    }
  });
  $e("$$ms-gr-react-wrapper", u), Ye(() => {
    _.set(Z(t));
  }), Ze(() => {
    b.forEach((d) => d());
  });
  function x(d) {
    J[d ? "unshift" : "push"](() => {
      l = d, g.set(l);
    });
  }
  function I(d) {
    J[d ? "unshift" : "push"](() => {
      s = d, c.set(s);
    });
  }
  return e.$$set = (d) => {
    o(17, t = q(q({}, t), Y(d))), "svelteInit" in d && o(5, a = d.svelteInit), "$$scope" in d && o(6, r = d.$$scope);
  }, t = Y(t), [l, s, g, c, i, a, r, n, x, I];
}
class nt extends Me {
  constructor(t) {
    super(), qe(this, t, tt, et, Je, {
      svelteInit: 5
    });
  }
}
const $ = window.ms_globals.rerender, N = window.ms_globals.tree;
function rt(e, t = {}) {
  function o(l) {
    const s = L(), n = new nt({
      ...l,
      props: {
        svelteInit(r) {
          window.ms_globals.autokey += 1;
          const i = {
            key: window.ms_globals.autokey,
            svelteInstance: s,
            reactComponent: e,
            props: r.props,
            slot: r.slot,
            target: r.target,
            slotIndex: r.slotIndex,
            subSlotIndex: r.subSlotIndex,
            ignore: t.ignore,
            slotKey: r.slotKey,
            nodes: []
          }, a = r.parent ?? N;
          return a.nodes = [...a.nodes, i], $({
            createPortal: W,
            node: N
          }), r.onDestroy(() => {
            a.nodes = a.nodes.filter((_) => _.svelteInstance !== s), $({
              createPortal: W,
              node: N
            });
          }), i;
        },
        ...l.props
      }
    });
    return s.set(n), n;
  }
  return new Promise((l) => {
    window.ms_globals.initializePromise.then(() => {
      l(o);
    });
  });
}
function ot(e) {
  const [t, o] = re(() => T(e));
  return oe(() => {
    let l = !0;
    return e.subscribe((n) => {
      l && (l = !1, n === t) || o(n);
    });
  }, [e]), t;
}
function st(e) {
  const t = B(() => ge(e, (o) => o), [e]);
  return ot(t);
}
const lt = ["animationIterationCount", "borderImageOutset", "borderImageSlice", "borderImageWidth", "boxFlex", "boxFlexGroup", "boxOrdinalGroup", "columnCount", "columns", "flex", "flexGrow", "flexPositive", "flexShrink", "flexNegative", "flexOrder", "gridArea", "gridColumn", "gridColumnEnd", "gridColumnStart", "gridRow", "gridRowEnd", "gridRowStart", "lineClamp", "lineHeight", "opacity", "order", "orphans", "tabSize", "widows", "zIndex", "zoom", "fontWeight", "letterSpacing", "lineHeight"];
function it(e) {
  return e ? Object.keys(e).reduce((t, o) => {
    const l = e[o];
    return t[o] = ct(o, l), t;
  }, {}) : {};
}
function ct(e, t) {
  return typeof t == "number" && !lt.includes(e) ? t + "px" : t;
}
function U(e) {
  const t = [], o = e.cloneNode(!1);
  if (e._reactElement) {
    const s = E.Children.toArray(e._reactElement.props.children).map((n) => {
      if (E.isValidElement(n) && n.props.__slot__) {
        const {
          portals: r,
          clonedElement: i
        } = U(n.props.el);
        return E.cloneElement(n, {
          ...n.props,
          el: i,
          children: [...E.Children.toArray(n.props.children), ...r]
        });
      }
      return null;
    });
    return s.originalChildren = e._reactElement.props.children, t.push(W(E.cloneElement(e._reactElement, {
      ...e._reactElement.props,
      children: s
    }), o)), {
      clonedElement: o,
      portals: t
    };
  }
  Object.keys(e.getEventListeners()).forEach((s) => {
    e.getEventListeners(s).forEach(({
      listener: r,
      type: i,
      useCapture: a
    }) => {
      o.addEventListener(i, r, a);
    });
  });
  const l = Array.from(e.childNodes);
  for (let s = 0; s < l.length; s++) {
    const n = l[s];
    if (n.nodeType === 1) {
      const {
        clonedElement: r,
        portals: i
      } = U(n);
      t.push(...i), o.appendChild(r);
    } else n.nodeType === 3 && o.appendChild(n.cloneNode());
  }
  return {
    clonedElement: o,
    portals: t
  };
}
function at(e, t) {
  e && (typeof e == "function" ? e(t) : e.current = t);
}
const O = de(({
  slot: e,
  clone: t,
  className: o,
  style: l,
  observeAttributes: s
}, n) => {
  const r = fe(), [i, a] = re([]), {
    forceClone: _
  } = be(), g = _ ? !0 : t;
  return oe(() => {
    var y;
    if (!r.current || !e)
      return;
    let c = e;
    function b() {
      let f = c;
      if (c.tagName.toLowerCase() === "svelte-slot" && c.children.length === 1 && c.children[0] && (f = c.children[0], f.tagName.toLowerCase() === "react-portal-target" && f.children[0] && (f = f.children[0])), at(n, f), o && f.classList.add(...o.split(" ")), l) {
        const h = it(l);
        Object.keys(h).forEach((u) => {
          f.style[u] = h[u];
        });
      }
    }
    let p = null;
    if (g && window.MutationObserver) {
      let f = function() {
        var I, d, C;
        (I = r.current) != null && I.contains(c) && ((d = r.current) == null || d.removeChild(c));
        const {
          portals: u,
          clonedElement: x
        } = U(e);
        c = x, a(u), c.style.display = "contents", b(), (C = r.current) == null || C.appendChild(c);
      };
      f();
      const h = Le(() => {
        f(), p == null || p.disconnect(), p == null || p.observe(e, {
          childList: !0,
          subtree: !0,
          attributes: s
        });
      }, 50);
      p = new window.MutationObserver(h), p.observe(e, {
        attributes: !0,
        childList: !0,
        subtree: !0
      });
    } else
      c.style.display = "contents", b(), (y = r.current) == null || y.appendChild(c);
    return () => {
      var f, h;
      c.style.display = "", (f = r.current) != null && f.contains(c) && ((h = r.current) == null || h.removeChild(c)), p == null || p.disconnect();
    };
  }, [e, g, o, l, n, s]), E.createElement("react-child", {
    ref: r,
    style: {
      display: "contents"
    }
  }, ...i);
});
function ut(e) {
  return /^(?:async\s+)?(?:function\s*(?:\w*\s*)?\(|\([\w\s,=]*\)\s*=>|\(\{[\w\s,=]*\}\)\s*=>|function\s*\*\s*\w*\s*\()/i.test(e.trim());
}
function dt(e, t = !1) {
  try {
    if (he(e))
      return e;
    if (t && !ut(e))
      return;
    if (typeof e == "string") {
      let o = e.trim();
      return o.startsWith(";") && (o = o.slice(1)), o.endsWith(";") && (o = o.slice(0, -1)), new Function(`return (...args) => (${o})(...args)`)();
    }
    return;
  } catch {
    return;
  }
}
function k(e, t) {
  return B(() => dt(e, t), [e, t]);
}
function ee(e, t) {
  const o = B(() => E.Children.toArray(e.originalChildren || e).filter((n) => n.props.node && !n.props.node.ignore && (!t && !n.props.nodeSlotKey || t && t === n.props.nodeSlotKey)).sort((n, r) => {
    if (n.props.node.slotIndex && r.props.node.slotIndex) {
      const i = T(n.props.node.slotIndex) || 0, a = T(r.props.node.slotIndex) || 0;
      return i - a === 0 && n.props.node.subSlotIndex && r.props.node.subSlotIndex ? (T(n.props.node.subSlotIndex) || 0) - (T(r.props.node.subSlotIndex) || 0) : i - a;
    }
    return 0;
  }).map((n) => n.props.node.target), [e, t]);
  return st(o);
}
function te(e, t) {
  return e ? /* @__PURE__ */ w.jsx(O, {
    slot: e,
    clone: t == null ? void 0 : t.clone
  }) : null;
}
function ne({
  key: e,
  slots: t,
  targets: o
}, l) {
  return t[e] ? (...s) => o ? o.map((n, r) => /* @__PURE__ */ w.jsx(G, {
    params: s,
    forceClone: !0,
    children: te(n, {
      clone: !0,
      ...l
    })
  }, r)) : /* @__PURE__ */ w.jsx(G, {
    params: s,
    forceClone: !0,
    children: te(t[e], {
      clone: !0,
      ...l
    })
  }) : void 0;
}
const pt = rt(({
  slots: e,
  children: t,
  render: o,
  filterOption: l,
  footer: s,
  listStyle: n,
  locale: r,
  onChange: i,
  onValueChange: a,
  setSlotParams: _,
  ...g
}) => {
  const c = ee(t, "titles"), b = ee(t, "selectAllLabels"), p = k(o), y = k(n), f = k(s), h = k(l);
  return /* @__PURE__ */ w.jsxs(w.Fragment, {
    children: [/* @__PURE__ */ w.jsx("div", {
      style: {
        display: "none"
      },
      children: t
    }), /* @__PURE__ */ w.jsx(xe, {
      ...g,
      onChange: (u, ...x) => {
        i == null || i(u, ...x), a(u);
      },
      selectionsIcon: e.selectionsIcon ? /* @__PURE__ */ w.jsx(O, {
        slot: e.selectionsIcon
      }) : g.selectionsIcon,
      locale: e["locale.notFoundContent"] ? {
        ...r,
        notFoundContent: /* @__PURE__ */ w.jsx(O, {
          slot: e["locale.notFoundContent"]
        })
      } : r,
      render: e.render ? ne({
        slots: e,
        setSlotParams: _,
        key: "render"
      }) : p || ((u) => ({
        label: u.title || u.label,
        value: u.value || u.title || u.label
      })),
      filterOption: h,
      footer: e.footer ? ne({
        slots: e,
        setSlotParams: _,
        key: "footer"
      }) : f || s,
      titles: c.length > 0 ? c.map((u, x) => /* @__PURE__ */ w.jsx(O, {
        slot: u
      }, x)) : g.titles,
      listStyle: y || n,
      selectAllLabels: b.length > 0 ? b.map((u, x) => /* @__PURE__ */ w.jsx(O, {
        slot: u
      }, x)) : g.selectAllLabels
    })]
  });
});
export {
  pt as Transfer,
  pt as default
};
